#include<graphics.h>
#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");

    // circle COLOR
    setcolor(WHITE);

    // First circle
    circle(200,70,25);    // circle(x-axis,y-axis,radious)

    setfillstyle(SOLID_FILL,WHITE);
    floodfill(201,71,WHITE);


    // Second Circle
    circle(235,60,30);    

    setfillstyle(SOLID_FILL,WHITE);
    floodfill(241,61,WHITE);


    // Third Circle
    circle(225,80,30);    

    setfillstyle(SOLID_FILL,WHITE);
    floodfill(226,91,WHITE);

    // Fourth Circle
    circle(260,70,30);    

    setfillstyle(SOLID_FILL,WHITE);
    floodfill(261,81,WHITE);


	getchar();
    return 0;
}