#include<graphics.h>
#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");

    for(int i=625; i>=-200; i--){
        outtextxy(i,200,"Hum-Suffer Express");
        delay(30);
    }

    


	getchar();
    return 0;
}