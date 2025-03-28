// Source: https://www.freecodecamp.org/learn/project-euler/project-euler-problems-1-to-100/problem-3-largest-prime-factor

/* 
Description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
*/


function largestPrimeFactor(number) 
{
  let largest = 0;

  while (number % 2 === 0)
  {
    number /= 2;
    largest = 2;
  }

  let factor = 3;
  let squared_n = Math.sqrt(number);
  while (factor <= squared_n)  
  {   
    if (number % factor === 0)
    {
      number /= factor;
      largest = factor;
    }
    else
    {
      factor += 2;
    }
  }
  return number >= factor ? number : largest;
}

module.exports = largestPrimeFactor;
