const websiteList = [
    'https://www.reddit.com',
    'https://www.vice.com',
    'https://www.moroccoworldnews.com',
    'https://www.nhl.com',
    'https://www.nba.com',
    'https://www.mlb.com',
    'https://www.cia.gov/library/publications/the-world-factbook/',
    'https://www.nfl.com',
    ]

const randomUrl = (list) =>{
  let i = Math.floor(Math.random() * list.length);
  return list[i]
}

// DOM selector
const rButton = document.querySelector('#redirect')

//event listener
rButton.addEventListener('click', (evt)=> {
  console.log('Bloooop');
  document.getElementById("frame").src = randomUrl(websiteList);

})
