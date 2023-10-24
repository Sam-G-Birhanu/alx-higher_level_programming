#include "main.h"
/**
 * _isalpha - shows 1 if the input is an
 * alphabet character. another cases show 0
 * @c: the character in AsCII mode
 *
 *  Return: 1 for lowercase, 0 for the rest
 */
int _isalpha(int c)
{
	if ((c  >= 65 &&  c <= 90) || (c >= 97 && c <= 122))
	{
		return (1);
	}
	else
	{
		return (0);
	}
	_putchar('\n');
}
