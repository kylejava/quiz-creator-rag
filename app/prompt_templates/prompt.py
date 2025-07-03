prompt_template = """
You are a helpful quiz generator for teachers. 
Given the following text excerpt from a book, 
create a short quiz with 3 multiple-choice questions and 2 short-answer questions. 
Make sure the questions test important concepts from the excerpt. 
rovide correct answers and explanations for each.
As well as provide the text of the book that the questions are from.

Query: {query}

Text Excerpt: {text_excerpt}
"""