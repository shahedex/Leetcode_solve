class Solution:
    def validIPAddress(self, IP: str) -> str:
        st = []
        count = 0
        if IP.count(':') > 1:
            st = IP.split(':')
            if len(st) != 8:
                return "Neither"
            for s in st:
                if len(s) < 1 or len(s) > 4:
                    return "Neither"
                x = 0
                for c in s:
                    if len(s) == 1 and s[0] == 0:
                        x += 1
                    elif (c >= 'a' and c <= 'f') or (c >= 'A' and c <= 'F'):
                        x += 1
                    elif (c >= '0' and c <= '9'):
                        x += 1
                    else:
                        return "Neither"
                count += 1
            if count == 8:
                return "IPv6"
            return "Neither"
        else:
            st = IP.split('.')
            if len(st) != 4:
                return "Neither"
            for s in st:
                try:
                    if len(s) == 1 and s[0] == '0':
                        count += 1
                    elif s[0] != '0' and int(s) >= 1 and int(s) <= 255:
                        count += 1
                    else:
                        return "Neither"
                except Exception:
                    return "Neither"
            if count == 4:
                return "IPv4"
            return "Neither"
        
        
# import re

# class Solution:

#     def validIPAddress(self, IP: str) -> str:
#         ip_v4 = r'^(?!0)([0-9]{1,3}\.?){3}(?!0)([0-9]{1,3})$'
#         ip_v6 = r'^([0-9a-fA-F]{1,4}:?){7}([0-9a-fA-F]{1,4})$'    
        
#         # IPV4
#         if re.match( ip_v4 , IP) :
#             if len( [ True for i in IP.split('.')  if int(i) < 256 ] ) == 4 :
#                 return "IPv4"

#          # IPV6
#         elif re.match( ip_v6 , IP ):
#             return "IPv6"

#         return "Neither"