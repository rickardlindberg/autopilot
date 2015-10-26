# Copyright (C) 2009-2015 Contributors as noted in the AUTHORS file
#
# This file is part of Autopilot.
#
# Autopilot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Autopilot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Autopilot.  If not, see <http://www.gnu.org/licenses/>.


from lib.instructions.base.instruction import Instruction
from lib.app.decorators import Overrides


class SelectMenuInstruction(Instruction):
    """
        select menu  (  arg1  ,  arg2  [ ,  arg]*  )

        arg     ::=  STRING | TEXT

        Select a menu in the the menu hierarchy, given by the args.
        At least 2 targets must be present.

        Example 1:   Select menu (Show, Sidebar)
        Example 2:   Select menu (Show, "Balloons on hover")
        Example 3:   Select Menu(File, New, "File Timeline...")
        Example 4:   Select Menu(Help, About | Om)
    """

    @Overrides(Instruction)
    def _execute(self):
        super(SelectMenuInstruction, self).select_menu()
