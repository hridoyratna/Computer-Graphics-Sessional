#include <iostream>
#include<stdio.h>
#include<graphics.h>

using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
    initgraph(&gd,&gm,"c:\\TURBOC3\\BGI");

    setcolor(YELLOW);
    outtextxy(150,150,"Hi !! Hridoy Ratno..");
    getchar ();
    return 0;
}