#include <bits/stdc++.h>
#include<graphics.h>
using namespace std;

int main() {
    int gd, gm;
    detectgraph(&gd, &gm);
    initgraph(&gd, &gm, "BGI");
    setcolor(GREEN);
    rectangle(100, 100, 250, 200);
    setfillstyle(XHATCH_FILL, GREEN);
    floodfill(101, 150, GREEN);
    outtextxy(100, 210, "Fig: Rectangle");
    getchar();
    return 0;
}