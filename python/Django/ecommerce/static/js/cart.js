// console.log("Hello, World!");
var updateBtns = document.getElementsByClassName("update-cart");
// console.log(updateBtns);

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        // console.log("You clicked");
        productId = this.dataset.product
        action = this.dataset.action

        if (user == 'AnonymousUser') {
            console.log("User is not logged in. Can't process the request");
        }
        else {
            updateRequest(productId, action)
        }
    })
}

function updateRequest(productId, action) {
    // console.log("User:", user, "| Processing request");
    // console.log("Product:", productId, "Action:", action);

    console.log("User is authenticated. Processing request ...")
    var url = '/update-request/'
    fetch(url, { 
        method: 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body: JSON.stringify({'productId' : productId, 'action' : action})
    })

    .then((response)=> {
        return response.json()
    })

    .then((data)=>{
        console.log('Data :', data)
        location.reload()
    })
}