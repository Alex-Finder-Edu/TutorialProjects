// Source: https://www.freecodecamp.org/learn/project-euler/project-euler-problems-1-to-100/problem-1-multiples-of-3-or-5

/* 
Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9, the sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below the provided parameter value number 
*/

function multiplesOf3Or5(number) 
{
    let sum = 0;
    for (let i=0; i < number; i++)
    {
      if (i % 3 == 0 || i % 5 == 0)
      {
        sum += i;
      }
    }
    return sum;
  }
  
  module.exports = multiplesOf3Or5;
  