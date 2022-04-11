import tkinter as tk
from tkinter import *
from tkinter import ttk
from PokeAPI import get_poke_info

def main():
    #window
    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap("Poke-Ball.ico")
    root['background'] = '#3466AF' 

    #window frames
    user_input_frame = tk.Frame(root)
    user_input_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    user_input_frame['background'] = '#FFCB05'

    info_frame = tk.LabelFrame(root, text="Info")
    info_frame.grid(row=1, column=0, padx=10, pady=10, sticky=N)
    info_frame['background'] = '#FFCB05'

    stats_frame = tk.LabelFrame(root, text="Stats")
    stats_frame.grid(row=1, column=1, padx=10, pady=10, sticky=N)
    stats_frame['background'] = '#FFCB05'

    #populate widgets in user input frame
    lbl_name = tk.Label(user_input_frame, text="Pokemon Name")
    lbl_name['background'] = '#FFCB05'
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    ent_name = ttk.Entry(user_input_frame)
    ent_name.grid(row=0, column=1, pady=10)

    def btn_get_info_click():
        #get pokemon info from the PokeAPI
        pokemon_name = ent_name.get()
        #display pokemon values
        poke_dictionary = get_poke_info(pokemon_name)
        if poke_dictionary:
            lbl_height_value["text"] = str(poke_dictionary["height"]) + " dm"
            lbl_weight_value["text"] = str(poke_dictionary["weight"]) + " hg"
            types_list = (t["type"]["name"] for t in poke_dictionary["types"])
            lbl_type_value["text"] = ', '.join(types_list)
            pb_hp_value["value"] = poke_dictionary["stats"][0]["base_stat"]
            pb_attack_value["value"] = poke_dictionary["stats"][1]["base_stat"]
            pb_defense_value["value"] = poke_dictionary["stats"][2]["base_stat"]
            pb_special_attack_value["value"] = poke_dictionary["stats"][3]["base_stat"]
            pb_special_defense_value["value"] = poke_dictionary["stats"][4]["base_stat"]
            pb_speed_value["value"] = poke_dictionary["stats"][5]["base_stat"]

    btn_get_info = tk.Button(user_input_frame, text="Get Info", command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10)

    #populate widgets in info frame
    lbl_height = ttk.Label(info_frame, text="Height:")
    lbl_height.grid(row=0, column=0, padx=10, pady=10, sticky=E)
    lbl_height['background'] = '#FFCB05'
    lbl_height_value = ttk.Label(info_frame)
    lbl_height_value.grid(row=0, column=1, padx=10, pady=10, sticky=W)
    lbl_height_value['background'] = '#FFCB05'

    lbl_weight = ttk.Label(info_frame, text="Weight:")
    lbl_weight.grid(row=1, column=0, padx=10, pady=10, sticky=E)
    lbl_weight['background'] = '#FFCB05'
    lbl_weight_value = ttk.Label(info_frame)
    lbl_weight_value.grid(row=1, column=1, padx=10, pady=10, sticky=W)
    lbl_weight_value['background'] = '#FFCB05'

    lbl_type = ttk.Label(info_frame, text="Type:")
    lbl_type.grid(row=2, column=0, padx=10, pady=10, sticky=E)
    lbl_type['background'] = '#FFCB05'
    lbl_type_value = ttk.Label(info_frame)
    lbl_type_value.grid(row=2, column=1, padx=10, pady=10, sticky=W)
    lbl_type_value['background'] = '#FFCB05'

    #populate widgets in stats frame
    lbl_hp = ttk.Label(stats_frame, text="HP:")
    lbl_hp.grid(row=0, column=0, padx=10, pady=10, sticky=E)
    lbl_hp['background'] = '#FFCB05'
    pb_hp_value = ttk.Progressbar(stats_frame, length=200, maximum=255)
    pb_hp_value.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    lbl_attack = ttk.Label(stats_frame, text="Attack:")
    lbl_attack.grid(row=1, column=0, padx=10, pady=10, sticky=E)
    lbl_attack['background'] = '#FFCB05'
    pb_attack_value = ttk.Progressbar(stats_frame, length=200, maximum=255)
    pb_attack_value.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    lbl_defense = ttk.Label(stats_frame, text="Defense:")
    lbl_defense.grid(row=2, column=0, padx=10, pady=10, sticky=E)
    lbl_defense['background'] = '#FFCB05'
    pb_defense_value = ttk.Progressbar(stats_frame, length=200, maximum=255)
    pb_defense_value.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    lbl_special_attack = ttk.Label(stats_frame, text="Special Attack:")
    lbl_special_attack.grid(row=3, column=0, padx=10, pady=10, sticky=E)
    lbl_special_attack['background'] = '#FFCB05'
    pb_special_attack_value = ttk.Progressbar(stats_frame, length=200, maximum=255)
    pb_special_attack_value.grid(row=3, column=1, padx=10, pady=10, sticky=W)

    lbl_special_defense = ttk.Label(stats_frame, text="Special Defense:")
    lbl_special_defense.grid(row=4, column=0, padx=10, pady=10, sticky=E)
    lbl_special_defense['background'] = '#FFCB05'
    pb_special_defense_value = ttk.Progressbar(stats_frame, length=200, maximum=255)
    pb_special_defense_value.grid(row=4, column=1, padx=10, pady=10, sticky=W)

    lbl_speed = ttk.Label(stats_frame, text="Speed:")
    lbl_speed.grid(row=5, column=0, padx=10, pady=10, sticky=E)
    lbl_speed['background'] = '#FFCB05'
    pb_speed_value = ttk.Progressbar(stats_frame, length=200, maximum=255)
    pb_speed_value.grid(row=5, column=1, padx=10, pady=10, sticky=W)
    

    root.mainloop()

main()