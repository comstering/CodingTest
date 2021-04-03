#include <stdio.h>
#include <stdlib.h>

void sort(int* numPtr, int count)
{
	int i, j;
	int temp;

	for (i = 0; i < count - 1; i++)
	{
		for (j = i + 1; j < count; j++)
		{
			if (*(numPtr + i) > *(numPtr + j))
			{
				temp = *(numPtr + i);
				*(numPtr + i) = *(numPtr + j);
				*(numPtr + j) = temp;
			}
		}
	}
}

int main(void)
{
	int count;
	int* numPtr;
	int num, i;

	scanf("%d", &count);

	if (count == 1)
	{
		scanf("%d", &num);
		num *= num;
	}
	else
	{
		numPtr = (int*)malloc(sizeof(int) * count);
		for (i = 0; i < count; i++)
			scanf("%d", numPtr + i);
		sort(numPtr, count);
		num = *numPtr * *(numPtr + count - 1);
		free(numPtr);
	}

	printf("%d", num);

	return 0;
}