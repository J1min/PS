#include <stdio.h> // 0으로 초기화 되어있다.
int data[100];     // 1 1 2 3 5 8 13 21 ......
int fibonacci(int x)
{
  if (x <= 2)
  {
    return 1;
  }
  if (data[x] != 0)
  { // 이미 계산을 해서 값이 가지고 있다.
    return data[x];
  }
  else
  { // 0이라는 것은 아직 계산이 된적이 없다는 것... // 계산을 하고 저장해둔다. // 그리고 값을 반환한다.
    data[x] = fibonacci(x - 1) + fibonacci(x - 2);
    return data[x];
  }
}
int main(void)
{
  printf("%d ", fibonacci(30));
  return 0;
}