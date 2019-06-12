# OSCP Buffer Overflow in 30 minutes

The scripts are based on [21y4d's work](https://github.com/21y4d/Windows_BufferOverflowx32) with additional automation and improvements lifted from Justin Steven's fantastic [dostackbufferoverflowgood tutorial](https://github.com/justinsteven/dostackbufferoverflowgood) &mdash; props to them.

The scripts are a bit rough (and are Python 2) but if you've read Justin Steven's guide, it should all make sense.

1. Start by modifying `constants.py` to include the `HOSTNAME` and `PORT` of the machine you are attacking.
2. You will also need to modify `send_payload()` so that the payload is properly sent to the vulnerable service; the example `send_payload()` interacts with an FTP server with the overflow in the password field.
3. Run the scripts in order, following the prompts and comments.

