# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_pathway_debate.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 10:16:47 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/16 10:43:51 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Absolute import:
import alchemy.transmutation.basic

# Relative Imports using __init__
import alchemy.transmutation

print("\n=== Pathway Debate Mastery ===")
print("\nTesting Absolute Imports (from basic.py):")
print(f"Lead_to_gold(): {alchemy.transmutation.basic.lead_to_gold()}")
print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}")
print("\nTesting Relative Imports (from advanced.py):")
print(f"philosophers_stone(): {alchemy.transmutation.advanced.philosophers_stone()}")
print(f"elixir_of_life(): {alchemy.transmutation.advanced.elixir_of_life()}")
print("\nTesting Package Access:")
print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")
print("\nBoth pathways work! Absolute: clear, Relative: concise")