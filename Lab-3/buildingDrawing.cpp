#include<graphics.h>
#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");

    setcolor(YELLOW);
    rectangle(100,50,250,300);
    setfillstyle(SOLID_FILL,YELLOW);
    floodfill(101,51,YELLOW);


    setcolor(WHITE);
    rectangle(150,100,200,150);
    setfillstyle(SOLID_FILL,WHITE);
    floodfill(151,101,WHITE);

    setcolor(WHITE);
    rectangle(150,200,200,250);
    setfillstyle(SOLID_FILL,WHITE);
    floodfill(151,201,WHITE);

	getchar();
    return 0;
}