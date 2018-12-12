"
                    "keys.  Otherwise, use the arguments as a list of keys "
                                        "(default is no legend).")
                                        parser.add_argument('--style', type=str, default='-',
                                                            help="point style, passed to plot function (default='-')")
# parser.add_argument('--exp10-x', action='store_const', const=True, default=False,
#                     help="raise x-axis to power of 10")
# parser.add_argument('--exp10-y', action='store_const', const=True, default=False,
#                     help="raise y-axis to power of 10")
# parser.add_argument('--log10-x', action='store_const', const=True, default=False,
#                     help="take log10 of x-axis")
# parser.add_argument('--log10-y', action='store_const', const=True, default=False,
#                     help="take log10 of y-axis")
parser.add_argument('--scale-x', type=float, default=1.0,
                    help="multiply variables on x-axis by this much (default=1)")
parser.add_argument('--scale-y', type=float, default=1.0,
                    help="multiply variables on y-axis by this much (default=1)")
parser.add_argument('--flip-x', action='store_true',
                    help="reverse the x-axis")
parser.add_argument('--flip-y', action='store_true',
                    help="reverse the y-axis")
parser.add_argument('--plotter', type=str, default='plot',
                    choices=['plot', 'semilogx', 'semilogy', 'loglog'],
                    help="use 'matplotlib.pyplot.plotter' to plot (default='plot')")
parser.add_argument('--title', type=str, nargs='+', default=[''],
                    help="Adds the given title to the plot.  Accepts spaces. "
                    "i.e. 'my plot' is OK.  Default is no title.")
                    parser.add_argument('--style-file', type=str, default=None,
                                        help="Specifies a matplotlib style file to load.")
parser.add_argument('--rcParams', type=str, nargs='+', default=[],
                    help="Any parameters in `matplotlib.pyplot.rcParams`, "
                    "provided in the form `key` `value`. "
                                        "e.g. --rcParams text.usetex True figure.dpi 300")
                                        # parser.add_argument('-v', '--verbose', action='store_true',
                                        #                     help="Print diagnostic information as plot is made.")

# skulduggery to put positional arguments first in usage
usage = parser.format_usage().split('\n')[:-1]
usage.insert(1, ' '*(len(parser.prog) + 8) + usage[0][usage[0].index('[-x'):])
usage[0] = parser.prog + ' [-h] ' + usage[-1].strip()
parser.usage = '\n'.join(usage[:-1])

args = parser.parse_args()

def vprint(*print_args):
    # if args.verbose:
    if False:
        print(*print_args)

vprint('Importing libraries... ')
import numpy as np
from matplotlib import pyplot as pl
vprint('Done.')

if args.style_file:
    vprint('Applying style file %s... ' % args.style_file)
    pl.style.use(args.style_file)
    vprint('Done.')
else:
    vprint('No style file requested.')

vprint("Selecting plotter '%s'..." % args.plotter)
if args.plotter == 'plot':
    plotter = pl.plot
elif args.plotter == 'semilogx':
    plotter = pl.semilogx
elif args.plotter == 'semilogy':
    plotter = pl.semilogy
elif args.plotter == 'loglog':
    plotter = pl.loglog
else:
    raise ValueError("invalid choice for --plotter "
                     "(but this should've been caught by argparse)")


                     vprint('Parsing `--rcParams`...')
                     i = 0
                     k = False
                     all_keys = list(pl.rcParams.keys())
                     while i < len(args.rcParams):
                         if not k:
                                 k = args.rcParams[i]
                                         i += 1
                                                 continue

                                                     s = args.rcParams[i]
                                                         if s in all_keys:
                                                                 raise ValueError("I didn't get an argument for "
                                                                                          "`rcParam` %s. " % k)

                                                                                              if type(pl.rcParams[k]) is bool:
                                                                                                      if s.lower() in ['true', 't']:
                                                                                                                  s = True
                                                                                                                          elif s.lower() in ['false', 'f']:
                                                                                                                                      s = False
                                                                                                                                              else:
                                                                                                                                                          raise ValueError("rcParam %s expects a boolean. "
                                                                                                                                                                                       "Please use `T`, `True`, `F` "
                                                                                                                                                                                                                    "or `False` (case insensitive)")

                                                                                                                                                                                                                        pl.rcParams[k] = type(pl.rcParams[k])(s
