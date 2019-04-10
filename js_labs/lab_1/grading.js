//grading.js
// let user_grade = parseInt(prompt("Please enter your grade"));
// let ones_digit = user_grade % 10
// console.log(user_grade);
// console.log(ones_digit);

//functions

const calculate = (x) => {
  let letter_grade = ''
  if (x < 60) {
    letter_grade = 'F'
  }
  else if (x > 59 && x < 70) {
    letter_grade = 'D'
  }
  else if (x > 69 && x < 80) {
    letter_grade = 'C'
  }
  else if (x > 79 && x < 90) {
    letter_grade = 'B'
  }
  else if (x > 89 && x <= 100) {
    letter_grade = 'A'
  }
  return letter_grade
}

const sign = (x) => {
  let grade_sign = ''
  if (x <= 4) {
    grade_sign = '-'
  }
  else if (x == 5) {
    grade_sign = ''
  }
  else if (x >= 6) {
    grade_sign = '+'
  }
  return grade_sign
}

// selectors
const convertBtn = document.querySelector('#convert')
const scoreInput = document.querySelector('#numericScore')
const letterGrade = document.querySelector('#letter-grade')
const scoreInputform = document.querySelector('#numeric-score')

//event listeners

convertBtn.addEventListener('click', (evt) =>{
  const x = parseInt(scoreInput.value)
  console.log(x)
  letter_grade = calculate(x)
  ones_digit = x % 10
  grade_sign = sign(ones_digit)
  console.log(letter_grade)
  letterGrade.value = `Your letter grade is ${letter_grade}${grade_sign}`
})

scoreInput.addEventListener('keydown', (evt) => {
  if (evt.key==='Enter') {
    const x = parseInt(scoreInput.value)
    console.log(x)
    letter_grade = calculate(x)
    ones_digit = x % 10
    grade_sign = sign(ones_digit)
    console.log(letter_grade)
    letterGrade.value = `Your letter grade is ${letter_grade}${grade_sign}`

  }
})
