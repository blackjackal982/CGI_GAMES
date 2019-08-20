const app = document.getElementById('root')

const logo = document.createElement('img')
logo.src = 'logo.jpg'

const container = document.createElement('div')
container.setAttribute('class', 'container')


app.appendChild(logo)
app.appendChild(container)

var request = new XMLHttpRequest()
request.open('GET', 'http://localhost:8000/games', true)
request.onload = function() {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
  if (request.status >= 200 && request.status < 400) {
    data.forEach(games => {
      const card = document.createElement('div')
      card.setAttribute('class', 'card')

      const h1 = document.createElement('h6')
      h1.textContent = games.title
      h1.setAttribute('class','card-header')

      const p = document.createElement('p')
      p.textContent = `Platform : ${games.platform}\r\nScore : ${games.score}\r\nGenre : ${games.genre}`
      if (games.editors_choice == 'Y')
      {
      p.textContent+=`\r\nEditors Choice : yes`
      }
      else
      {
      p.textContent+=`\r\nEditors Choice : no`
      }
      container.appendChild(card)
      card.appendChild(h1)
      card.appendChild(p)
    })
  } else {
    const errorMessage = document.createElement('marquee')
    errorMessage.textContent = `Gah, it's not working!`
    app.appendChild(errorMessage)
  }
}

request.send()