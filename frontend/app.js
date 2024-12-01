async function fetchProducts() {
    const response = await fetch('http://localhost:5000/api/products');
    const products = await response.json();
    const productList = document.getElementById('product-list');
    
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.innerHTML = `<h2>${product.name}</h2><p>${product.description}</p><p>Preço: $${product.price}</p>`;
        productList.appendChild(productDiv);
    });
}

fetchProducts();
