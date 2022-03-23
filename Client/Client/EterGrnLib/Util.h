//Lorderon Client Binary Dev by Lordbecvold
#pragma once

bool GrannyMeshIsDeform(granny_mesh* pgrnMesh);
class CGraphicImage;
struct SMaterialData
{
	CGraphicImage * pImage;
	float fSpecularPower;
	BOOL isSpecularEnable;
	BYTE bSphereMapIndex;
};

