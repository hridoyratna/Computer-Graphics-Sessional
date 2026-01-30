#include <bits/stdc++.h>
#include<graphics.h>
using namespace std;

int main() {
    int gd, gm;
    detectgraph(&gd, &gm);
    initgraph(&gd, &gm, "BGI");
    setcolor(BLUE);
    circle(200, 200, 80);
    setfillstyle(SOLID_FILL, BLUE);
    floodfill(201, 201, BLUE);
    outtextxy(150, 290, "Fig: Circle Drawing");
    getchar();
    return 0;
}