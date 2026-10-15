import pyvista as pv

try:
    print("🔄 Testando o PyVista...")
    
    cylinder = pv.Cylinder(radius=1.0, height=5.0, resolution=36)
    
    print("\n✅ PyVista e VTK carregados com sucesso!")
    print(f"- Número de vértices (pontos): {cylinder.n_points}")
    print(f"- Número de faces (células): {cylinder.n_cells}")
    print(f"- Volume aproximado: {cylinder.volume:.2f}")

    # 1. Cria a "janela" do estúdio sem abrir uma interface gráfica real
    plotter = pv.Plotter(off_screen=True)
    # 2. Coloca o cilindro dentro da janela
    plotter.add_mesh(cylinder)
    # 3. Guarda a cena com o cilindro, luzes e câmaras num ficheiro GLTF
    plotter.export_gltf("teste_vaso.gltf")
    # 4. Fecha o plotter para libertar a memória RAM do servidor
    plotter.close()
    
    print("\n🚀 Exportação GLTF realizada com sucesso! O arquivo 'teste_vaso.gltf' foi criado.")

except Exception as e:
    print(f"\n❌ Ocorreu um erro no PyVista: {e}")