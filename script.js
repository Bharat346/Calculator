const exp = require("express");
const app = exp();
const cors = require("cors")

app.use(cors());

// web scrapping code 
fetch("https://cprakash86.wordpress.com/csbb101-pscb/")
.then(res => res.text())
.then(html =>{
  const parser = new DOMParser();
  const doc = parser.parseFromString(html,'text/html')

  // Extracting title 
  const title = doc.querySelector('title').textContent
  //console.log(title)

  //Extracting all links
  const links = Array.from(doc.querySelectorAll('a')).map(link => link.href)
  //console.log('links:',links);

  // Extracting all paras
  const paras = Array.from(doc.querySelectorAll('p')).map(para => para.textContent)
  //console.log("paras:",paras[1])
  
  //  Extracting all images
  const img = Array.from(doc.querySelectorAll("img")).map(img => img.src)
  //console.log("Images : ",img[0]);

  //console.log(html)
  
  //  Extracting all news
  const n1 = doc.querySelector('.n1');
  if(n1){
    const content = n1.textContent.trim();
    //console.log("News : ",content);
  }
  else{
    //console.log('News was not found');
  }

})
.catch(e =>{
  console.log("Error in Fetching Data : ",e);
})