

function renderDresses(category = 'all') {
    shopItems.innerHTML = '';
    dresses.forEach(dress => {
        if (category === 'all' || dress.category === category) {
            const item = document.createElement('div');
            item.classList.add('shop-item');
            item.innerHTML = `
                <img src="${dress.image}" alt="${dress.name}">
                <h3>${dress.name}</h3>
                <p>ราคา: ${dress.price} บาท</p>
            `;
            shopItems.appendChild(item);
        }
    });
}

categoryFilter.addEventListener('change', () => {
    renderDresses(categoryFilter.value);
});

renderDresses(); // แสดงชุดทั้งหมดเมื่อโหลดหน้าเว็บ