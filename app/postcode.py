# -*- coding: utf-8 -*-
# 12/05/17 Job application task
# 
# Author: Matthew Golab
# 
# Part 1 - Postcode validation
 
# Imports
import re
import unittest

# Use re.compile("""()""", re.X) to make expression more readable over several lines.
regular_expression = r"""(GIR\s0AA) | 
                           (    
                                # A9 or A99 prefix
                                ( ([A-PR-UWYZ][0-9][0-9]?) |
                                    # AA99 prefix with some excluded areas
                                    (
                                        ([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |
                                        # AA9 prefix with some excluded areas
                                        ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |
                                        # WC1A prefix
                                        (WC[0-9][A-Z]) |
                                        (
                                            # A9A prefix
                                            ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                                            # AA9A prefix
                                            ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
                                        )
                                    )
                                )
                                # 9AA suffix
                                \s[0-9][ABD-HJLNP-UW-Z]{2}
                            )"""


class Postcode(object):
    def __init__(self, regex_in):
        # For optimisation compile in given regex and pass in using raw string notation (instead of string literal) with 'r'.
        # Use re.compile("""()""", re.X) to make expression more readable over several lines.
        self.regex = re.compile(regex_in, re.X)

    def TestPostCode(self, postcode):
        if not re.fullmatch(self.regex, postcode):
            return False
        else:
            return True



