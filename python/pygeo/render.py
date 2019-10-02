import numpy as np
import vtk
from vtk.util import numpy_support as nsp


def meshshow(V: np.ndarray, F: np.ndarray):
    mesh = vtk.vtkPolyData()
    points = vtk.vtkPoints()
    cells = vtk.vtkCellArray()

    points.SetData(nsp.numpy_to_vtk(V))
    n, dim = F.shape
    tmp = np.concatenate(
        [np.ones((n, 1), dtype=np.int64) * dim, F], axis=1).flatten()
    cells.SetCells(n, nsp.numpy_to_vtkIdTypeArray(tmp))

    mesh.SetPoints(points)
    mesh.SetPolys(cells)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(mesh)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    camera = vtk.vtkCamera()
    camera.SetPosition(1, 1, 1)
    camera.SetFocalPoint(0, 0, 0)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetActiveCamera(camera)
    renderer.ResetCamera()

    win = vtk.vtkRenderWindow()
    win.AddRenderer(renderer)
    win.SetSize(500, 500)

    interact = vtk.vtkRenderWindowInteractor()
    interact.SetRenderWindow(win)
    interact.Start()
