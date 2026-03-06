import re
import asyncio
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv(override=True)

llm = ChatGroq(model="openai/gpt-oss-20b")


class Person(BaseModel):
    Imo_number: str = Field(description="The IMO Number")
    Name_of_yard: str = Field(description="The company's name")
    Country: str = Field(description="The country name")
    Hull_number: str = Field(description="The Hull number")


def filter_detail(data):

    prompt = """
    You are an expert in extracting details using an below data.
    Your task is to search and return the following information exactly as found
    from verified ship-building sources (no hallucination):

    Imo_number, Name_of_yard, Country, Hull_number.

    Return clean JSON format:
    Example:
    {"Imo_number": "1074644", "Name_of_yard": "Qingdao Yangfan Shipbuilding Co. Ltd.", "Country": "China", "Hull_number": "210K DWT BC-08"}

    Source: {source}
    """

    parser = JsonOutputParser(pydantic_object=Person)

    prompt = PromptTemplate(
        template=prompt,
        input_variables=["source"]
    )

    chain = prompt | llm | parser
    result = chain.invoke({"source": data})

    return result


async def extract_ship_info(imo_number: str):

    url = f"https://www.trusteddocks.com/vessel/{imo_number}"

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:

            response = await page.goto(url, timeout=60000)

            if response is None or not response.ok:
                return None

            raw_text = await page.inner_text("body")
            cleaned_text = re.sub(r"\n+", "\n", raw_text).strip()

            return cleaned_text

        finally:
            await browser.close()


async def get_ship_details(imo):

    text = await extract_ship_info(imo)

    if text is None:
        return None

    result = filter_detail(text)

    return result