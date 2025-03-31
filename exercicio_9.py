def set_cover(warehouses, stores):
    selected_warehouses = []
    uncovered_stores = set(stores)
    
    while uncovered_stores:
        best_warehouse = None
        covered_stores = set()

        for warehouse, coverage in warehouses.items():
            new_coverage = uncovered_stores & coverage
            if len(new_coverage) > len(covered_stores):
                best_warehouse = warehouse
                covered_stores = new_coverage
        
        if best_warehouse is None:
            break  
        selected_warehouses.append(best_warehouse)
        uncovered_stores -= covered_stores  
    return selected_warehouses

warehouses = {
    "A": {"L1", "L2", "L3"},
    "B": {"L2", "L4"},
    "C": {"L3", "L5"},
    "D": {"L4", "L5", "L6"},
    "E": {"L6"}
}

stores = {"L1", "L2", "L3", "L4", "L5", "L6"}

solution = set_cover(warehouses, stores)
print("Armazéns selecionados:", solution)
