quest novyhrac begin
    state start begin
        when login with pc.get_playtime() == 0 begin
            notice_all("P�i�el nov� hr��: "..pc.get_name())
        end
    end
end