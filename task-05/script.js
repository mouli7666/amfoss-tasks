-This is the script I have written for task-05



document.addEventListener('DOMContentLoaded', () => {
    
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then(products => {
            const productListing = document.querySelector('.product-listing');
            products.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('product');
                productDiv.innerHTML = `
                    <img src="${product.image}" alt="${product.title}">
                    <h3>${product.title}</h3>
                    <p>Original Price: <span style="color: red;">$${(product.price * 1.2).toFixed(2)}</span></p>
                    <p>Discounted Price: <span style="color: green;">$${product.price.toFixed(2)}</span></p>
                    <button> Add to Cart </button>
                `;
                productListing.appendChild(productDiv);
            });
        })
        .catch(error => console.error('Error fetching products:', error));

    
    const terminalInput = document.getElementById('terminal-input');
    const terminalOutput = document.querySelector('.terminal-output');

    terminalInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            const command = terminalInput.value.trim();
            handleInput(command);
            terminalInput.value = ''; 
        }
    });

    function handleInput(command) {
        switch (command.toLowerCase()) {
            case 'help':
                viewCommand();
                break;
            case 'list':
                listProducts();
                break;
            case 'clear':
                terminalOutput.textContent = '';
                break;
            default:
                terminalOutput.textContent += `Invalid command: ${command}\n`;
                break;
        }
    }

    function viewCommand() {
        terminalOutput.innerHTML += "Available Commands:\n- list: List all products\n- clear: Clear the screen\n- help: View all commands\n";
    }

    function listProducts() {
        fetch('https://fakestoreapi.com/products')
            .then(res => res.json())
            .then(products => {
                products.forEach(product => {
                    terminalOutput.textContent += `${product.title} - $${product.price}\n`;
                });
            })
            .catch(error => terminalOutput.textContent += `Error fetching products: ${error}\n`);
    }
});
