#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int size, i;
	int* numPtr;
	int position = 0;
	int sum = 0;

	scanf("%d", &size);
	numPtr = (int*)malloc(sizeof(int) * size);

	for (i = 0; i < size; i++)
	{
		scanf("%d", numPtr + position);
		if (*(numPtr + position) == 0)
		{
			position--;
			continue;
		}
		position++;
	}

	for (i = 0; i < position; i++)
		sum += *(numPtr + i);

	printf("%d", sum);

	free(numPtr);

	return 0;
}