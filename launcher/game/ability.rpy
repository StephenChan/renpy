# Checks for various abilities that might be taken away from us by 
# redistributors.

init 1 python in ability:
    
    from store import config
    import renpy.store as store
    
    import os
    
    EXECUTABLES = [ "renpy.exe", "renpy.app", "renpy.sh" ]
    
    # can_distribute - True if we can distribute 
    for i in EXECUTABLES:
        if not os.path.exists(os.path.join(config.renpy_base, i)):
            can_distribute = False
    else:
        can_distribute = True
        
        
    # can_update - True if we can update.
    can_update = os.path.exists(os.path.join(config.renpy_base, "update/current.json")) or (store.UPDATE_SIMULATE is not None)
    
