
# Copyright Aleksey Gurtovoy 2001-2006
#
# Distributed under the Boost Software License, Version 1.0. 
# (See accompanying file LICENSE_1_0.txt or copy at 
# http://www.boost.org/LICENSE_1_0.txt)
#
# See http://www.boost.org/libs/mpl for documentation.

# $Id: preprocess_vector.py 49269 2008-10-11 06:30:50Z agurtovoy $
# $Date: 2008-10-11 02:30:50 -0400 (Sat, 11 Oct 2008) $
# $Revision: 49269 $

import preprocess
import os.path

preprocess.main(
      [ "no_ctps", "plain", "typeof_based" ]
    , "vector"
    , os.path.join( "boost", "mpl", "vector", "aux_", "preprocessed" )
    )
