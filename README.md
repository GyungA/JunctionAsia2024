# M. Mom Eat

AI-powered web service that helps pregnant women quickly check whether certain foods are safe to eat.

## Overview

Pregnancy often comes with many dietary restrictions, making it difficult for pregnant women to determine whether certain foods are safe to consume. Information online can be scattered or unclear.

**M. Mom Eat** is a web service that allows users to search for food items and receive instant AI-generated guidance about whether those foods are safe during pregnancy.

This project was **designed, developed, and deployed independently within 3 days during the Junction Asia Hackathon**.

---

## Key Features

**Food Safety Search**  
Users can search for specific foods and receive pregnancy-related safety information.

**AI-powered Responses**  
Integrated the **ChatGPT API** to generate contextual answers for food safety queries.

**Response Caching**  
Generated answers are parsed and stored in the database so that repeated searches can return faster results without calling the API again.

**Fast Prototyping**  
Built and deployed a functional full-stack service within a limited hackathon timeframe.

---

## Tech Stack

**Backend**
- Python
- Django

**Frontend**
- Tailwind CSS

**AI Integration**
- OpenAI ChatGPT API

**Database**
- SQLite

---

## System Flow

1. User searches for a food item  
2. Server checks whether the result already exists in the database  
3. If not found, the backend sends a request to the ChatGPT API  
4. The response is parsed and stored in the database  
5. Cached results are reused for future searches to reduce API calls and improve response speed

---

## Architecture

```

User
↓
Django Backend
↓
Database (cached responses)
↓
OpenAI ChatGPT API

```

---

## Motivation

This project explores how **AI-powered services can simplify everyday health-related decisions** by making information more accessible.

By combining **AI APIs with backend caching logic**, the system improves both **response speed and user experience**.

---

## Future Improvements

- Expand the food safety database with verified medical sources  
- Add user personalization features  
- Improve validation of AI-generated responses  
- Deploy production infrastructure (AWS / Docker)

<img width="1317" alt="스크린샷 2024-08-11 오전 11 47 30" src="https://github.com/user-attachments/assets/c1aad893-5f74-4651-97bd-8c1f5e2515b4">
<img width="1317" alt="스크린샷 2024-08-11 오전 11 47 42" src="https://github.com/user-attachments/assets/77c07ec5-d907-481e-97f9-d103104de40f">
