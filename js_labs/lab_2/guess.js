
const computerChoice = Math.floor(Math.random() * 11)
let counter = 0
let computerResponse = ''
let guessCorrect = false
//functions

const checkNumber = (computerChoice, userGuess) => {
  if (computerChoice < userGuess) {
    counter ++
    result.value = "That wasn't it, try a lower number!"

  }
  else if (computerChoice > userGuess) {
    counter ++
    result.value = "That wasn't it, try a higher number!"

  }
  else if (computerChoice === userGuess) {
    counter ++
    result.value = `Yes, that was it! It only took ${counter} tries. `
    guessCorrect = true

  }

  return guessCorrect
}



// selectors
const submitBtn = document.querySelector('#submit')
const userGuess = document.querySelector('#userGuess')
const result = document.querySelector('#result')
//event listeners

submitBtn.addEventListener('click', (evt) =>{
  const x = parseInt(userGuess.value)
  console.log(x)
  guessCorrect = checkNumber(computerChoice, x)
  console.log(guessCorrect)
  guessCorrect.value = `${computerResponse}`
  if (computerChoice === userGuess) {
    userGuess = 'userGuess.value'
  } else if (computerChoice != userGuess) {
    userGuess.value = ''
  }

})

userGuess.addEventListener('keydown', (evt) => {
  if (evt.key==='Enter') {
  const x = parseInt(userGuess.value)
  console.log(x)
  guessCorrect = checkNumber(computerChoice, x)
  console.log(guessCorrect)
  guessCorrect.value = `${computerResponse}`
  if (computerChoice === userGuess) {
    userGuess.value = userGuess.value
  } else if (computerChoice != userGuess) {
    userGuess.value = ''
  }
}
})
