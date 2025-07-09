from langchain_core.prompts import PromptTemplate
from app.utils.llm import get_llm
from sqlalchemy.orm import Session
from app.models.recommendation import Recommendation

template = """
You are an expert e-commerce assistant.

Based on:
- Browsing history: {history}
- Avg time on products: {avg_time}
- Cart items: {cart_items}
- Past purchases: {purchases}
- Budget: {budget}

Suggest two product types the user may like and explain why.
"""

prompt = PromptTemplate.from_template(template)

def predict_customer_interest(db: Session, data: dict) -> str:
    llm = get_llm()
    chain = prompt | llm
    response = chain.invoke(data)

    # Handle AIMessage object by extracting content
    if hasattr(response, "content"):
        response = response.content

    # Store in DB
    db_record = Recommendation(**data, response=response)
    db.add(db_record)
    db.commit()

    return response
