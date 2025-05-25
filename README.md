# 🛍️ Product Selection API

A simple FastAPI project connected to MongoDB that allows users to:

- 📦 Fetch product details by `product_id`
- 🎨 Select color and size for a specific product (with validation)

---

## 🚀 Tech Stack

- **FastAPI** — Web framework for building APIs
- **Pydantic** — Data validation
- **MongoDB** — NoSQL database to store product data
- **PyMongo** — Python driver for MongoDB

---

## 📁 Project Structure

```
.
├── main.py         # FastAPI app with endpoints
├── models.py       # Pydantic models for data validation
└── README.md       # Project overview
```

---

## 📦 Sample Product Schema

```json
{
  "product_id": "TSHIRT123",
  "name": "Cotton T-shirt",
  "description": "Comfortable cotton T-shirt",
  "available_colors": ["red", "blue", "black"],
  "available_sizes": ["S", "M", "L", "XL"],
  "price": 499,
  "units_left": 20,
  "image_url": "https://example.com/images/tshirt.jpg",
  "product_url": "https://example.com/products/TSHIRT123"
}
```

---

## 🔧 Installation & Run

**Install dependencies:**
```bash
pip install fastapi pymongo uvicorn
```

**Run the server:**
```bash
uvicorn main:app --reload
```

**Open API docs:**  
Visit [http://localhost:8000/docs](http://localhost:8000/docs) to explore the Swagger UI.

---

## 🛠️ API Endpoints

### `GET /products/{product_id}`

Returns full product details.

**Example:**
```bash
GET /products/TSHIRT123
```

---

### `POST /products/select`

Validates user-selected color and size for a product.

**Request Body:**
```json
{
  "product_id": "TSHIRT123",
  "selected_color": "red",
  "selected_size": "M"
}
```

**Successful Response:**
```json
{
  "message": "Product selection successful",
  "product_id": "TSHIRT123",
  "selected_color": "red",
  "selected_size": "M"
}
```