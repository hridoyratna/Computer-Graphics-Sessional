#include <bits/stdc++.h>
#include<graphics.h>
using namespace std;

int main() {
    int gd, gm;
    detectgraph(&gd, &gm);
    initgraph(&gd, &gm, "BGI");
    setcolor(RED);
    line(100, 150, 200, 150);
    line(200, 150, 150, 80);
    line(100, 150, 150, 80);
    setfillstyle(INTERLEAVE_FILL, RED);
    floodfill(150, 140, RED);
    outtextxy(100, 160, "Fig: Triangle");
    getchar();
    return 0;
}