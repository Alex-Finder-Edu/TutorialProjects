// Source: https://www.freecodecamp.org/learn/project-euler/project-euler-problems-1-to-100/problem-3-largest-prime-factor

/* 
Description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
*/

function is_prime(n)
{
 
  for (let i = 2; i<= Math.sqrt(n); i++){
    if ( n % i === 0 ) {
      return false;}
  }
  return true;
}

function largestPrimeFactor(number) {

  for (let i = Math.round(Math.sqrt(number)); i >= 2; i--){
    if (number % i == 0 && is_prime(i)) {
      return i;
    }
  }
  return number;
}

module.exports = largestPrimeFactor;
