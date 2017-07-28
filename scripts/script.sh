# Download from archive.noao.edu: simple query form: PI=forster; observing calendar date between 2015-01-01 and 2015-12-31.
# A total of ~1.5TB of images. This script finds the relevant ones and deletes the rest.

fitsheader -e 0 --keyword OBJECT -t ascii.tab *.fits.fz>list.tsv

grep Blind list.tsv |awk '{print $4}'|sort|uniq|xargs mkdir

foreach joe (`grep Blind list.tsv |awk '{print $4}'|sort|uniq`)
  grep $joe list.tsv |awk '{print $1}'|xargs -I '{}' mv -v '{}' $joe

mkdir zri; mv -v *_zri.fits.fz zri
mkdir fri; mv -v *_fri.fits.fz fri
mkdir ori; mv -v *_ori.fits.fz ori
mkdir fci; mv -v *_fci_*.fits.fz fci
mkdir fcw; mv -v *_fcw_*.fits.fz fcw
mkdir zci; mv -v *_zcw_*.fits.fz zcw
mkdir zcw; mv -v *_zci_*.fits.fz zci
mkdir ici; mv -v *_ici_*.fits.fz ici

mkdir tmpkeep
mv -v Blind15A_26 tmpkeep
mv -v Blind15A_40 tmpkeep
mv -v Blind15A_42 tmpkeep

rm -rv Blind*
mv tmpkeep/Blind* .
rmdir tmpkeep

fitsheader -e 0 --keyword PROCTYPE -t ascii.tab */*.fits.fz >list_PROCTYPE.tsv
mkdir MasterCal
grep MasterCal list_PROCTYPE.tsv | awk '{print $1}' | xargs -I '{}' cp -v '{}' MasterCal/

# Don't need the 'wtmap' mastercals or the illumcor files:
#rm -v MasterCal/*_fcw_* MasterCal/*_zcw_* MasterCal/*_ici_*

fitsheader -e 0 --keyword EXPNUM --keyword FILTER -t ascii.tab Blind15A_*/*.fits.fz > list_EXPNUM_FILTER.tsv
