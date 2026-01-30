#include<graphics.h>
#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");

    
    for(int j=400; j>=-100; j--){
        setcolor(RED);
        circle(200,j,30);
        setfillstyle(SOLID_FILL,RED);
        floodfill(201,j,RED);
        delay(30);
        cleardevice();
    }


    


	getchar();
    return 0;
}