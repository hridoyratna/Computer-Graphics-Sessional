#include<graphics.h>
#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");

    setcolor(GREEN);
    rectangle(50,50,220,150);
    setfillstyle(SOLID_FILL,GREEN);
    floodfill(51,51,GREEN);

    setcolor(WHITE);
    rectangle(40,40,50,300);
    setfillstyle(SOLID_FILL,WHITE);
    floodfill(41,41,WHITE);

    setcolor(RED);
    circle(130,100,30);
    setfillstyle(SOLID_FILL,RED);
    floodfill(131,101,RED);


	getchar();
    return 0;
}