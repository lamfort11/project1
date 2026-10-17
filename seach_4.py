def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    import util
    hang_doi_uu_tien = util.PriorityQueue()
    start_state = problem.getStartState()
    
    chi_phi_bat_dau = 0
    do_uu_tien_bat_dau = chi_phi_bat_dau + heuristic(start_state, problem)
    
    hang_doi_uu_tien.push((start_state, [], chi_phi_bat_dau), do_uu_tien_bat_dau)
    da_duyet = set()
    
    while not hang_doi_uu_tien.isEmpty():
        state, actions, chi_phi_hien_tai = hang_doi_uu_tien.pop()
        
        if problem.isGoalState(state):
            return actions
            
        if state not in da_duyet:
            da_duyet.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in da_duyet:
                    chuoi_hanh_dong_moi = actions + [action]
                    tong_chi_phi_moi = chi_phi_hien_tai + stepCost
                    
                    do_uu_tien_moi = tong_chi_phi_moi + heuristic(successor, problem)
                    
                    hang_doi_uu_tien.push((successor, chuoi_hanh_dong_moi, tong_chi_phi_moi), do_uu_tien_moi)
                    
    return []
