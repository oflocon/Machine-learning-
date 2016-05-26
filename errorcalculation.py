def computeErrorForLineGivenPoints(b, m, pts):
    tError = 0
    for i in range(0, len(pts)):
        tError += (pts[i].y - (m * pts[i].x + b)) ** 2
    return tError / float(len(pts))
