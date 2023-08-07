<!__doc__.asyncio import asyncio
import os
from cryptography.fernet import Fernet
async def main():
    with open("C:\\Users\\user\\.config\\my-app\\secret", "rb
              ") as key:
        f = Fernet(key)
        print(f"Encrypted file content:\n{f.decrypt(open('C:\\Users
              \\user\\Desktop/important_file', 'r').read().encode())}")
        if __name__ == "__main__":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
            </pre>
            </details><br/>
            <h3 id="cryptography.fernet.Fernet.encrypt"><code class
            >cryptography.fernet.Fernet.encrypt</code></h3>
            <p>Encrypts the plaintext using this fernet instance.</p>
            <div class=highlight>
            <span></span><table style="border-spacing:0px;padding:0px
            ">
            <tr>
            <td colspan=2>&nbsp;<br/><b>Parameters:</b><hr/></td
            ></tr>
            <tr>
            <td valign="top"><tt class="docutils literal">plaintext<font
            ><span class="pre">*</span></font></tt></td>
            <td>The data to encrypt, which must be bytes or a bytearray.<br/>
            </td></tr>
            <tr>
            <td colspan=2>&nbsp;</td></tr>
            <tr>
            <td colspan=2>&nbsp;<br/><b>Returns:</b><hr/></td
            ></tr>
            <tr>
            <td valign="top"><tt class="docutils literal">bytes</tt></td>
            <td>A binary string of encrypted data that can safely stored on disk and passed around in
            memory without risking corruption due to tampering or deletion by an attacker.<br/>
            </td></tr>
            <tr>
            <td colspan=2>&nbsp;</td></tr>
            <tr>
            <td colspan=2>&nbsp;<br/><b>Raises :</b><ul>
            <li><tt class="xref py py-exc docutils literal">TypeError</tt>: If
            any argument is not valid for encryption (e.g., it contains non-ASCII text).</
            li>
            <li><tt class="xref py py-exc docutils literal">ValueError</tt>: If
            no arguments are provided when calling ``encrypt``.</li>
            </ul></td></tr>
            </table>
            </div>
            <dl class="method">
            <dt id="cryptography.fernet.Fernet.__init__">
            <em class="property">classmethod </em><code class="">__init__(self)</code
            ></dt>
            <dd>Initialize self.&nbsp;&nbsp;&nbsp;See help(<a href="#crypto
                                                           ryptography.fernet.Fernet" title="cryptography.fernet.
                                                           ryptography.fernet.Fernet" title="(in Python v3.6
                                                           )">cryptography.fernet.Fernet</a>)
            for accurate signature.</dd>
            </dl>
            </div>
            </div>
            </div>
            </div>
            </body>
            </html>
            """
            ),
            ],
            },
            }
            )
            return(doc)
            else:
            print("No documentation found")
            
            except Exception as e :
            #print(str(type(e)))    # the exception instance
            print('ERROR:', str(e))      # __str__ allows args to be printed directly
            ,
            exit()
            