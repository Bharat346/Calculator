document.addEventListener("DOMContentLoaded", () => {
  // Fetch news from an API
  fetch(
    "https://newsapi.org/v2/top-headlines?country=in&apiKey=96b036858f1f4f57b10e8d7569479277"
  )
    .then((response) => response.json())
    .then((data) => {
      const newsContainer = document.getElementById("news-container");
      const newsContainer2 = document.getElementById("news-container2");
      const newsContainer3 = document.getElementById("news-container3");
      // Iterate through each article and create HTML elements

      const articleElement = document.createElement("div");
      articleElement.className = "news-article";

      const imageElement = document.createElement("div");
      imageElement.className = "news-image";
      imageElement.innerHTML = `<img src="${data.articles[4].urlToImage}" alt="News Image" style="width: 100%;">`;

      const descriptionElement = document.createElement("div");
      descriptionElement.className = "news-description";
      descriptionElement.innerHTML = `
            <div class="news-title">${data.articles[4].title}</div>
            <p>${data.articles[4].description}</p>
            <a href="${data.articles[4].url}" class="news-link" target="_blank">Read More</a>
        `;

      articleElement.appendChild(imageElement);
      articleElement.appendChild(descriptionElement);
      newsContainer.appendChild(articleElement);

      // sports
      const articleElement2 = document.createElement("div");
      articleElement2.className = "news-article";

      const imageElement2 = document.createElement("div");
      imageElement2.className = "news-image";
      imageElement2.innerHTML = `<img src="${data.articles[5].urlToImage}" alt="News Image" style="width: 100%;">`;

      const descriptionElement2 = document.createElement("div");
      descriptionElement2.className = "news-description";
      descriptionElement2.innerHTML = `
            <div class="news-title">${data.articles[5].title}</div>
            <p>${data.articles[5].description}</p>
            <a href="${data.articles[5].url}" class="news-link" target="_blank">Read More</a>
        `;

      articleElement2.appendChild(imageElement2);
      articleElement2.appendChild(descriptionElement2);
      newsContainer2.appendChild(articleElement2);

      // film
      const articleElement3 = document.createElement("div");
      articleElement3.className = "news-article";

      const imageElement3 = document.createElement("div");
      imageElement3.className = "news-image";
      imageElement3.innerHTML = `<img src="${data.articles[8].urlToImage}" alt="News Image" style="width: 100%;">`;

      const descriptionElement3 = document.createElement("div");
      descriptionElement3.className = "news-description";
      descriptionElement3.innerHTML = `
            <div class="news-title">${data.articles[8].title}</div>
            <p>${data.articles[8].description}</p>
            <a href="${data.articles[8].url}" class="news-link" target="_blank">Read More</a>
        `;

      articleElement3.appendChild(imageElement3);
      articleElement3.appendChild(descriptionElement3);
      newsContainer3.appendChild(articleElement3);
    })
    .catch((error) => console.error("Error fetching news:", error));
  // Trigger fetching news when the page loads
  //document.addEventListener('DOMContentLoaded', fetchNews);

  // set quote
  const motContainer = document.getElementById("mot");
  // Fetch the quote of the day from ZenQuotes API
  fetch("https://api.quotable.io/random")
    .then((response) => response.json())
    .then((data) => {
      // Check if the API response contains the 'content' property (quote text)
      if (data.content) {
        // Create a paragraph element to display the quote
        const quoteParagraph = document.createElement("p");
        quoteParagraph.textContent = data.content;

        // Clear existing content in the container
        motContainer.innerHTML = "";

        // Append the quote paragraph to the container
        motContainer.appendChild(quoteParagraph);
      } else {
        // If the API response does not contain the 'content' property, display an error message
        motContainer.innerHTML =
          "Failed to fetch a random quote. Please try again later.";
      }
    })
    .catch((error) => {
      // Handle any fetch errors
      console.error("Error fetching a random quote:", error);
      motContainer.innerHTML =
        "Failed to fetch a random quote. Please try again later.";
    });

  // set cookie
  function setCookie(name, value, days) {
    var expires = "";
    if (days) {
      var date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
  }

  // Call the setCookie function with your desired values
  setCookie("visitedPortfolio", "true", 365);
});
