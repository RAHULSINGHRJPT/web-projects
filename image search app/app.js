const accesskey = "rnRxfdA5J1fRZOwR3O3yVsTx5yZhoYekfMNP6-E_664";
const formElement = document.querySelector("form");
const searchinputElement = document.getElementById("search-input");
const searchResultsElement = document.querySelector(".search-results");//use dot because it is a class 
const showMoreButtonElement = document.getElementById("show-more-button");

let inputData = "";
let page = 1;

async function searchImages() {
    inputData = searchinputElement.value;
    const url = `https://api.unsplash.com/search/photos?page=${page}&query=${inputData}&redirect_uri=urn:ietf:wg:oauth:2.0:oob&client_id=${accesskey}`;
  
    const response = await fetch(url);
    const data = await response.json();
    if(page===1){
      searchResultsElement.innerHTML="";
    }
    const result = data.results;

    result.map((result)=>{

      const imageWrapper = document.createElement("div");
      imageWrapper.classList.add("search-results");
      const image = document.createElement("img");
      image.src = result.urls.small;
      image.alt=result.alt_description;

      const imageLink = document.createElement("a");
      imageLink.href = result.links.html;
      imageLink.target="_blank";
      imageLink.textContent = result.alt_description;

      imageWrapper.appendChild(image);
      imageWrapper.appendChild(imageLink);
      searchResultsElement.appendChild(imageWrapper);
    });

    page++;

    if(page>1){
      showMoreButtonElement.style.display = "block";
    }

  console.log(results);
  }
  
  

formElement.addEventListener("submit",(event)=>{
    event.preventDefault();
    page = 1;
    searchImages();
});

showMoreButtonElement.addEventListener("click", (event)=>{
  searchImages();
})










