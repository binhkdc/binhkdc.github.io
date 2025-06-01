const container = document.querySelector('.container');
const messages = [
    "bé iu 1/6 vui vẻ nhoa",
    "Chúc Cáo iu 1/6 vui vẻ nhoa",
    "My love <3",
    "Chúc bé iu 1/6 vui vẻ nhoa",
    // Thêm các biến thể khác nếu muốn
];

// Bạn cần có các icon mèo/cáo thực tế. Có thể dùng ảnh (png/svg) hoặc font icon.
// Đối với ví dụ này, tôi sẽ dùng một placeholder màu vàng.
// Để có icon giống hình, bạn sẽ cần các file ảnh PNG/SVG cho icon mèo/cáo
// và thay thế trong phần CSS hoặc tạo <img> tag ở đây.
const iconCountOptions = [1, 2, 3, 4]; // Số lượng icon trong một nhóm

function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

function createFloatingElement(type) {
    const element = document.createElement('div');
    if (type === 'message') {
        element.classList.add('message-item');
        element.textContent = messages[Math.floor(Math.random() * messages.length)];
    } else if (type === 'icon') {
        element.classList.add('icon-group');
        const count = iconCountOptions[Math.floor(Math.random() * iconCountOptions.length)];
        for (let i = 0; i < count; i++) {
            const icon = document.createElement('div');
            icon.classList.add('icon');
            element.appendChild(icon);
        }
    }

    // Đặt vị trí ban đầu ngẫu nhiên dưới màn hình
    const startX = getRandomArbitrary(0, 90); // 0% đến 90% chiều rộng màn hình
    const animationDuration = getRandomArbitrary(8, 15); // Thời gian animation ngẫu nhiên
    const delay = getRandomArbitrary(0, 5); // Độ trễ khởi tạo ngẫu nhiên

    element.style.left = `${startX}vw`;
    element.style.animationDuration = `${animationDuration}s`;
    element.style.animationDelay = `${delay}s`;
    // Dùng custom property để truyền giá trị ngẫu nhiên vào keyframes
    element.style.setProperty('--rand-x', getRandomArbitrary(-0.5, 0.5)); // Để có sự di chuyển ngang ngẫu nhiên

    container.appendChild(element);

    // Xóa phần tử sau khi animation kết thúc để tránh tạo quá nhiều DOM
    element.addEventListener('animationend', () => {
        element.remove();
    });
}

// Tạo liên tục các phần tử
setInterval(() => {
    createFloatingElement('message');
    if (Math.random() > 0.5) { // 50% cơ hội tạo icon group
        createFloatingElement('icon');
    }
}, 500); // Tạo một phần tử mới mỗi 0.5 giây