function searchURL(){
    window.location.href = "/catalog/products?q="+document.getElementById("search_main").value;
    return false;
}

function clearSearch(){
    window.location.href = "?q=";
    return false;
}