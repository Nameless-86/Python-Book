#include "stdio.h"

// int base, altura;

int area(int base, int altura);

void main(void)
{
    // printf("Ingresar la longitud de la base: ");
    // scanf("%d", &base);
    // printf("Ingresar la longitud de la altura: ");
    // scanf("%d", &altura);
    // printf("El area del rectangulo es: %d\n", area(base, altura));
    // printf("La cantidad de bytes de int es: %d\n", sizeof(int));
    // printf("La cantidad de bytes de float es: %d\n", sizeof(float));
    // printf("La cantidad de bytes de double es: %d\n", sizeof(double));
}

int area(int base, int altura)
{
    int area;
    area = base * altura;
    return area;
}
